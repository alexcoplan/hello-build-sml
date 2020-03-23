from configure import BuildEnv

def describe(env : BuildEnv) -> None:
  env.Program('myprog', 'MyProg.main', 'myproglib.cm')
  env.Test('mytest', 'MyTest.main', 'mytest.cm')
