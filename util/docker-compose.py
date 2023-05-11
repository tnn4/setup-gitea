import sys, os
import subprocess

docker_compose_file_test= "./docker-gitea-compose-test.yml"
docker_compose_file="./docker-gitea-compose.yml"
me=os.path.basename(__file__)
UP="up"
DOWN="down"

def start_with(_arg):
    
    match _arg:
        case "up":
            print("starting docker services required for gitea")
            if use_test==True:
                subprocess.run(["docker","compose", "-f", docker_compose_file_test, UP])
            else:
                subprocess.run(["docker","compose", "-f", docker_compose_file, UP])
            #fi
        case "down":
            print("stopping docker services required for gitea")
            if use_test==False:
                subprocess.run(["docker","compose", "-f", docker_compose_file_test, DOWN ])
            else:
                subprocess.run(["docker","compose", "-f", docker_compose_file, DOWN ])
            #fi
    #end-match
#fed

if __name__ == "__main__":
    # subprocess.run(["docker","compose", "-f", docker_compose_file, "up"])
    if len(sys.argv) == 2: # 1 arguments
        print("argv[1] = " + sys.argv[1])
        arg=sys.argv[1]
        if arg != UP or arg != DOWN:
            print("[{_me}:ERROR] requires argument: < up|down >".format(_me=me))
        #fi
    else:
        print("[{_me}:ERROR] requires 1 or 2 argument: < up [-t] |down >".format(_me=me))
        print(" -t runs docker-gitea-compose-test.yml")
    #fi

    use_test=False;

    if len(sys.argv) == 3: # 2 arguments
        if sys.argv[1] == UP and sys.argv[2] == "-t":
            use_test=True
        #fi
    #fi

    arg=sys.argv[1]
    start_with(arg)
#endmain