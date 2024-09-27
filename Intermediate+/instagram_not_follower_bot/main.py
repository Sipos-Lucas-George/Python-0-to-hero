"""
    Instagram Bot That Shows The Users That Do Not Follow You Back
"""
import subprocess


def run_script(script_path):
    return subprocess.Popen(['python', script_path])


script1_path = "/home/lucas/Desktop/Intermediate+/instagram_not_follower_bot/followers.py"
script2_path = "/home/lucas/Desktop/Intermediate+/instagram_not_follower_bot/following.py"

# process1 = run_script(script1_path)
# process2 = run_script(script2_path)
#
# process1.wait()
# process2.wait()

print("\nBoth scripts have finished.")

with open("following.txt") as file:
    following = file.readlines()
following = set([f.strip() for f in following])

with open("followers.txt") as file:
    followers = file.readlines()
followers = set([f.strip() for f in followers])

with open("not_following_back.txt", "w") as file:
    for item in following.difference(followers):
        file.write(item + "\n")
print(following.difference(followers))
