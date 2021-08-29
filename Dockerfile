FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ UTC

#Install APT Apps
RUN apt-get update -qq && apt-get install -qqy \
		bat \
		calcurse \
		cmus \
		ctop \
		figlet \
		git \
		glances \
		hollywood \
		make \
		neofetch \
		nload \
		nmon \
		ranger \
		taskwarrior \
		tty-clock && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
	dpkg-reconfigure tzdata && \
	updatedb

#Install GIT Apps
RUN git clone https://github.com/pipeseroni/pipes.sh.git && \
	make install -C pipes.sh/ && \
	rm -rf pipes.sh/
