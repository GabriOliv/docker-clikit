# ~/.bashrc: executed by bash(1) for non-login shells.
[ -z "$PS1" ] && return
HISTCONTROL=ignoredups:ignorespace
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s checkwinsize
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    # PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    PS1='\[\e[1m\][\[\e[1;38;5;39m\]\u\[\e[m\]\[\e[1m\]][\[\e[1;32m\]\A\[\e[m\]\[\e[1m\]]:\[\e[m\]\w\[\e[1m\]\$\[\e[m\]'

else
    # PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
    PS1='\[\e[1m\][\[\e[1;38;5;39m\]\u\[\e[m\]\[\e[1m\]][\[\e[1;32m\]\A\[\e[m\]\[\e[1m\]]:\[\e[m\]\w\[\e[1m\]\$\[\e[m\]'
fi
unset color_prompt force_color_prompt

case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias bat='batcat'
alias clock-figlet='while true; do clear; echo "$(date '+%T' | figlet -ct)"; echo "[Ctrl+C] to EXIT"; sleep 1; done'
alias dockerfetch='neofetch --ascii /etc/guides/docker_logo.txt  --ascii_colors 12 15 14 --colors 4 14 12 6 15 8'
alias histcat='history|grep'
alias guide='python3 /etc/guides/guide.py'
alias taskhelp='cat /etc/guides/taskwarrior_guide.txt'

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
