# !/bin/bash
# 主要任务
# 文件的未更新时间确定
# firefox的重启和关闭

file="file.txt"
now_time=$(date +%s)
modify_time=$(stat -c %Y $file)
echo $now_time
echo $modify_time


while true
do
now_time=$(date +%s)
modify_time=$(stat -c %Y $file)
echo $now_time
echo $modify_time
if (($(($now_time -$modify_time)) > 1000));
then
echo "do something"
else
echo "It's not a good time!!!"
fi
sleep 10s
done

auto_pid=$(ps -ef|grep auto.py|grep -v color|grep -v grep|awk '{print $2}')
echo "auto_pid: $auto_pid"
# kill $auto_pid

firefox_pid=$(ps -ef |grep firefox|grep -v contentproc|grep -v color|grep -v grep|awk '{print $2}')
echo "firefox_pid: $firefox_pid"
## kill $firefox
# killall geckodriver



# open a new auto_Linux.py
# nohup python3.9 auto_Linux.py > runout.log 2>&1 &
