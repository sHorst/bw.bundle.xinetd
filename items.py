
# start service
svc_systemd['xinetd.service'] = {
    'needs': ['pkg_apt:xinetd', ],
}
