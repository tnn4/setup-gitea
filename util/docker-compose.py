import sys
import subprocess

docker_compose_file_test= "./docker-gitea-compose-test.yml"
docker_compose_file="./docker-gitea-compose.yml"
UP="up"
DOWN="down"

if __name__ == "__main__":
    # subprocess.run(["docker","compose", "-f", docker_compose_file, "up"])
    if len(sys.argv) == 2:
        print(sys.argv[1])
        arg=sys.argv[1]
        if arg != "up" or arg != "down":
            print("[ERROR] requires argument: < up|down >")
        #endif
    else:
        print("[ERROR] requires 1 or 2 argument: < up [-t] | down >")
        print(" -l option will run image with log file permissions added")
    #endif

    use_test=False;
    if len(sys.argv) == 3:
        if sys.argv[1] == UP and sys.argv[2] == "-t":
            use_test=True
        #fi
    #fi

    arg=sys.argv[1]
    match arg:
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
#endmain