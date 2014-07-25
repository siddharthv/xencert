The XenServer Storage Certification Kit
=======================================

This repository contains the code of the "XenServer storage Certification Kit".

Build and Install
=================

This repository is typically delivered as an ISO that needs to be installed on
each host independently. This ISO can be installed by the CLI via:
`xe-install-supplemental-pack `path to <xencert-supp-pack.iso>`

Commmand Line Switches and Options
==================================

Usage: XenCert [arguments seen below]

Common options:

 -f functional                  [optional] perform functional tests
 -c control                     [optional] perform control path tests
 -m multipath                   [optional] perform multipath configuration verification tests
 -o pool                        [optional] perform pool verification tests
 -d data                        [optional] perform data verification tests
 -M metadata                    [optional] perform metadata tests
 -h help                        [optional] show this help message and exit

Storage specific options:

 Storage type lvmoiscsi:

 -t target                      [required] comma separated list of Target names/IP addresses
 -q targetIQN                   [required] comma separated list of target IQNs OR "*"
 -s SCSIid                      [optional] SCSIid to use for SR creation
 -x chapuser                    [optional] username for CHAP
 -w chappasswd                  [optional] password for CHAP

 Storage type nfs:

 -n server                      [required] server name/IP addr
 -e serverpath                  [required] exported path

 Storage type lvmohba:

 -a adapters                    [optional] comma separated list of HBAs to test against

 Storage type isl:

 -F file                        [required] configuration file describing target array paramters

Test specific options:
Multipathing test options (-m above):

 -b storage_type                [required] storage type (lvmoiscsi, lvmohba, nfs, isl)
 -u pathHandlerUtil             [optional] absolute path to admin provided callout utility which blocks/unblocks a list of paths, path related information should be provided with the -i option below
 -i pathInfo                    [optional] pass-through string used to pass data to the callout utility above, for e.g. login credentials etc. This string is passed as-is to the callout utility.
 -g count                       [optional] count of iterations to perform in case of multipathing failover testing

XenCert Help: `/opt/xensource/debug/XenCert/XenCert -h`
