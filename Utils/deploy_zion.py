import os

host = "10.30.223.232"
user = "zion"
password = "zion"

# os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/swift/middleware', user, host, 'josep/zion/swift'))

# os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/compute/runtime/java/bin/zion-runtime-1.0.jar', user, host, 'josep/zion/runtime/java/'))

os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/compute/service', user, host, 'josep/zion'))

# os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/compute/runtime/java/start_daemon.sh', user, host, 'josep/zion/runtime/java/'))

# os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/compute/runtime/java/lib', user, host, 'josep/zion/runtime/java/'))
# os.system('sshpass -p %s scp -r %s %s@%s:%s' % (password, '../Engine/compute/runtime/java/logback.xml', user, host, 'josep/zion/runtime/java/'))

print "--> FILES UPLOADED"

os.system('sshpass -p %s ssh %s@%s "%s" > /dev/null' % (password, user, host, 'sudo josep/copy_zion.sh'))

print "--> FINISH"
