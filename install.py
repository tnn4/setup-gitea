import sys
import subprocess

# docker_compose_file="./docker-gitea-compose-v3.yml"

if __name__ == "__main__":
    
    # $ source util/cp-no-bin; run-from-project-root
    # python's subprocess can't run `source` so we use a workaround
    # run bash with the raw string, extraordinarily hacky but linux lets us do these sorts of things
    cmd_str="bash -c \"source util/cp-no-bin; run-from-project-root\""
    # subprocess.run(cmd_str, shell=True)
    #end-match
    if len(sys.argv) == 2:
        print("passed in {argc} argument".format(argc=len(sys.argv)-1))
        # remove last character which is a quote, see: https://stackoverflow.com/questions/15478127/remove-final-character-from-string
        cmd_str=cmd_str[:-1]
        # add the argument
        cmd_str=cmd_str+ " " + sys.argv[1] + "\""
        print("cmd: {_cmd_str}".format(_cmd_str=cmd_str))
        subprocess.run(cmd_str, shell=True)
    else:
        print("passed in 0 arguments, using defaults")
        print("cmd: {_cmd_str}".format(_cmd_str=cmd_str))
        subprocess.run(cmd_str, shell=True)
    #endif
#endmain