# -*- coding: utf-8 -*-
import signal, os, subprocess, sys, os.path, multiprocessing

def alarm_handler(signum, frame):
  print 'Signal handler called with signal', signum
  salir(1)

signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(30)

def salir(codigo, kill = False):
  try:
    master.kill()
  except:
    pass
  try:
    jug.kill()
  except:
    pass
  try:
    com.terminate()
  except:
    pass
  if kill:
    os.kill(0,codigo)
  sys.exit(0)

if (len(sys.argv)!=2):
  print "conn.py <jugador.py> "
  sys.exit(1)

jugador_exe = sys.argv[0]
if (jugador_exe.find(" ")==-1 and not os.path.exists(jugador_exe)):
  print "No encuentro el ejecutable " + jugador_exe
  sys.exit(1)


master_exe = "master.py"
if (not os.path.exists(master_exe)):
  print "No encuentro el ejecutable " + master_exe
  sys.exit(1)

master = subprocess.Popen("python2.7 -u master.py" ,
                         bufsize=1,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         close_fds=True)
(master_stdin, master_stdout) = (master.stdin, master.stdout);

jug = subprocess.Popen("python2.7 -u programa.py",
                       bufsize=1,
                       shell=True,
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       close_fds=True)
(jug_stdin, jug_stdout) = (jug.stdin, jug.stdout);

def connect(read_from_pipe, write_to_pipe, debug_msg, master_to_jug):
  line = "="
  while (not master_to_jug or line.strip()!=".") and line.strip()!="":
    try:
      line = read_from_pipe.readline().strip()
      line = line.strip()
    except:
      print ">Error de comunicacion %s" % debug_msg
      sys.exit(1)
    if not master_to_jug or line.strip()!="":
      try:
          print >> write_to_pipe, line
          print ">>" if master_to_jug else "<", line,
#        write_to_pipe.write(line)
      except:
        pass
  return line.strip()==""

def connect2(read_from_pipe, write_to_pipe, debug_msg, master_to_jug):
  line = "="
  try:
     line = read_from_pipe.readline().strip()
  except:
      print ">Error de comunicacion %s" % debug_msg
      sys.exit(1)
  if not master_to_jug or line.strip()!="":
      print ">>" if master_to_jug else "<", line
      try:
          print >> write_to_pipe, line
#        write_to_pipe.write(line)
      except:
        print 'Falle'
  return line

def communicate():
  linea = "1"
  while linea != '':
    linea = connect2(master_stdout, jug_stdin, "master->jug", True)
    linea = connect2(jug_stdout, master_stdin, "jug->master", False)
  # Last line: score.
  #print ">", master_stdout.readline(),
#==============================================================================
#   sys.stdout.flush()
#   jug.kill()
#   sys.exit(0)
#==============================================================================


com = multiprocessing.Process(target=communicate)
com.start()
retval = jug.wait()
com.join()

if retval != 0 and retval != -9:
    salir(retval-128, kill=True)
else:
    salir(0)
