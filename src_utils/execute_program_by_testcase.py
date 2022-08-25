import subprocess
import sys


def run_program_by_testinput(source_code="name=input()\nprint(f'Hello {name}!')",testinput="World\n"):
    try:
        results = subprocess.run([sys.executable, "-c", source_code],
                                 input=testinput.replace("\r\r", '') + '\n',
                                 universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 timeout=15)
        output = results.stdout.rstrip()
        print(output)
    except:
        pass


def run_program_by_testinput_and_save_coverage_info(source_code_filename,testinput,save_output_directory):
    try:
        subprocess.run([sys.executable, "-m", "trace", "--count", "--coverdir",
                        save_output_directory, "-c", source_code_filename],
                        input=testinput.replace("\r\r", '') + '\n',
                        universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        timeout=15)
    except:pass

