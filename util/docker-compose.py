import sys
import subprocess

docker_compose_file="./docker-gitea-compose-v3.yml"

if __name__ == "__main__":
    # subprocess.run(["docker","compose", "-f", docker_compose_file, "up"])
    if len(sys.argv) == 2:
        print(sys.argv[1])
        arg=sys.argv[1]
        if arg != "up" or arg != "down":
            print("[ERROR] requires argument: < up|down >")
        #endif
    else:
        print("[ERROR] requires 1 argument: < up|down >")
    #endif

    arg=sys.argv[1]
    match arg:
        case "up":
            print("starting docker services required for gitea")
            subprocess.run(["docker","compose", "-f", docker_compose_file, "up"])
        case "down":
            print("stopping docker services required for gitea")
            subprocess.run(["docker","compose", "-f", docker_compose_file, "down"])
    #end-match
#endmain