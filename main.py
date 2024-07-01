import time
import sys
import os

def main():
  f = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Real time LaTeX editor</title><script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script></head><body><h1>MathJax Example</h1><p>\( ENTER LATEX HERE \)</p></body></html>'
  last_inp = "ENTER LATEX HERE"
  ls = os.listdir()
  if len(sys.argv) != 2 or sys.argv[1] not in ls:
    print("Error:\nUsage: lated [LaTeX file]")
    exit()
  print(f"[{sys.argv[1]}] found")
  with open(sys.argv[1], "r") as l:
    print(f"[{sys.argv[1]}] opened")
  with open("index.html", "w") as w:
    w.write(f)
  print(f"[index.html] has been created")
  while True:
    try:
        with open(sys.argv[1], "r") as l:
          lat = l.read()
    except FileNotFoundError:
        pass
    if lat:
      with open("index.html", "r") as wr:
        a = wr.read().replace(last_inp, lat)
      with open("index.html", "w") as ww:
        ww.write(a)
      last_inp = lat
    time.sleep(0.5)

try:
  main()
except KeyboardInterrupt:
  print("Exiting...")
  exit()
