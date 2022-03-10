FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ UTC

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install apt apps
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
		micro \
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

# Install git apps
RUN git clone https://github.com/pipeseroni/pipes.sh.git && \
	make install -C pipes.sh/ && \
	rm -rf pipes.sh/

# Copy scripts
COPY docs/scripts/ /etc/clikit

# Copy bashrc
COPY docs/.bashrc /root/