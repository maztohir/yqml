from args import Args

def main():
  job_name = args.input
  print(job_name)

if __name__ == '__main__':
  args = Args.parse()
  main()
