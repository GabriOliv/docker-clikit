FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ UTC

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


# Install APT Apps
RUN apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get update -qq && apt-get install -qqy \
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

# Install GIT Apps
RUN git clone https://github.com/pipeseroni/pipes.sh.git && \
	make install -C pipes.sh/ && \
	rm -rf pipes.sh/

# Copy Scripts and Guides
COPY docs/clikit_essentials /etc/

# Copy Bashrc Alias and PS1 changes
COPY docs/.bashrc /root/
