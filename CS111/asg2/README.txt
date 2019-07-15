build and install the kernel using
make kernelbuild KERNCONF=CUSTOM
make kernelinstall KERNCONF=CUSTOM
(use sudo make if not running as root)

if this fails (as I struggled making this makefile) use
svn checkout https://svn.freebsd.org/base/releng/11.2 /usr/src
rm src/sys/sys/runq.h src/sys/kern/kern_switch.c src/sys/kern/sched_ule.c
    src/sys/kern/subr_param.c
mv runq.h src/sys/sys
mv subr_param.c kern_switch.c sched_ule.c src/sys/kern
mv CUSTOM sys/amd64/conf

then re-use the above commands using freeBSD's makefile
(again use sudo if not root)

switch scheduling styles at runtime with sysctl
sysctl priority_sched = 0 (priority off)
sysctl priority_sched = 1 (priority on)
sysctl splatter_sched = 0 (splatter off)
sysctl splatter_sched = 1 (splater on)

splatter and priority are default turned off

I did this assignment by myself, so there are no group members to condsider
