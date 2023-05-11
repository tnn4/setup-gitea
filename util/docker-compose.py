import sys
import subprocess

docker_compose_file= "./docker-gitea-compose-v3.0.yml"
docker_compose_file2="./docker-gitea-compose-v3.1.yml"
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
        print("[ERROR] requires 1 or 2 argument: < up|down > [-l]")
        print(" -l option will run image with log file permissions added")
    #endif

    test=False;
    if len(sys.argv) == 3:
        if sys.argv[2] == "-l":
            test=True
        #fi
    #fi

    arg=sys.argv[1]
    match arg:
        case "up":
            print("starting docker services required for gitea")
            if test==True:
                subprocess.run(["docker","compose", "-f", docker_compose_file2, UP])
            else:
                subprocess.run(["docker","compose", "-f", docker_compose_file, UP])
            #fi
        case "down":
            print("stopping docker services required for gitea")
            if test==False:
                subprocess.run(["docker","compose", "-f", docker_compose_file2, DOWN ])
            else:
                subprocess.run(["docker","compose", "-f", docker_compose_file, DOWN ])
            #fi
    #end-match
#endmain