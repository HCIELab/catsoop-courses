import sys
import time
import shutil
import signal
import hashlib
import resource
import threading
import subprocess

_resource_mapper = {
    'CPUTIME': (resource.RLIMIT_CPU, lambda x: (x, x + 1)),
    'MEMORY': (resource.RLIMIT_AS, lambda x: (x, x)),
    'FILESIZE': (resource.RLIMIT_FSIZE, lambda x: (x, x)),
}


class PKiller(threading.Thread):
    def __init__(self, proc, timeout):
        threading.Thread.__init__(self)
        self.proc = proc
        self.timeout = timeout

    def run(self):
        end = time.time() + self.timeout
        while (time.time() < end):
            time.sleep(0.1)
            if self.proc.poll() is not None:
                return
        if self.proc.poll() is not None:
            os.killpg(os.getpgid(self.proc.pid), signal.SIGKILL)


def compile_code(context, code, options):
    rlimits = []
    for key, val in _resource_mapper.items():
        if key == 'MEMORY' and options[key] <= 0:
            continue
        rlimits.append((val[0], val[1](options[key])))
    def limiter():
        os.setsid()
        for i in rlimits:
            resource.setrlimit(*i)

    tmpdir = context.get('csq_sandbox_dir', '/tmp/cpp_sandbox')
    tmpdir = '/tmp/cpp_sandbox'
    this_one = hashlib.sha512(('%s-%s' % (context.get('cs_username', 'None'), time.time())).encode()).hexdigest()
    tmpdir = os.path.join(tmpdir, this_one)
    libdir = os.path.join(tmpdir, 'lib')
    os.makedirs(tmpdir, 0o777)
    for f in options['FILES']:
        typ = f[0].strip().lower()
        if typ == 'copy':
            shutil.copyfile(f[1], os.path.join(libdir, f[2]))
        elif typ == 'string':
            with open(os.path.join(libdir, f[1]), 'w') as f:
                f.write(f[2])
    fname = '%s.cpp' % this_one
    oname = '%s.o' % this_one
    with open(os.path.join(tmpdir, fname), 'w') as f:
        f.write(code.replace('\r\n', '\n'))

    compiler = context.get('csq_compiler', 'g++')
    #'-static',
    p = subprocess.Popen([compiler, '-o', oname,  '-L%s' % libdir, fname],
                         cwd=tmpdir,
                         preexec_fn=limiter,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    killer = PKiller(p, options['CLOCKTIME'])
    killer.start()

    out, err = p.communicate(options['STDIN'])
    out = out.decode()
    err = err.decode()
    if p.returncode != 0:
        shutil.rmtree(tmpdir, True)

    return this_one, out, err, p.returncode


def run_code(context, name, options):
    rlimits = [(resource.RLIMIT_NPROC, (0, 0))]
    for key, val in _resource_mapper.items():
        if key == 'MEMORY' and options[key] <= 0:
            continue
        rlimits.append((val[0], val[1](options[key])))
    def limiter():
        os.setsid()
        for i in rlimits:
            resource.setrlimit(*i)

    tmpdir = context.get('csq_sandbox_dir', '/tmp/cpp_sandbox')
    tmpdir = '/tmp/cpp_sandbox'
    tmpdir = os.path.join(tmpdir, name)
    fname = os.path.join(tmpdir, '%s.o' % name)
    p = subprocess.Popen([fname] + options.get('ARGS', []),
                         cwd=tmpdir,
                         preexec_fn=limiter,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    killer = PKiller(p, options['CLOCKTIME'])
    killer.start()

    out, err = p.communicate(options['STDIN'])
    out = out.decode()
    err = err.decode()
    shutil.rmtree(tmpdir, True)

    return out, err, p.returncode
