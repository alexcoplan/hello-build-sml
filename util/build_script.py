import subprocess

logbuf = ""
def log(msg):
  global logbuf
  logbuf += msg

def logln(msg):
  global logbuf
  logbuf += (msg + "\n")

def fail():
  print(logbuf)
  exit(1)

def run(cmd, **kwargs):
  log("Running " + " ".join(cmd) + " ... ")
  res = subprocess.run(cmd, capture_output=True, **kwargs)
  if res.returncode == 0:
    logln("OK")
    return
  logln("FAILED")
  stdout = res.stdout.decode("utf-8").strip()
  stderr = res.stderr.decode("utf-8").strip()
  if len(stdout) > 0:
    logln("Output (stdout):")
    log(stdout)
  if len(stderr) > 0:
    logln("Output (stderr):")
    log(stderr)

  fail()
