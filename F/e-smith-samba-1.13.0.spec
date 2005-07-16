Summary: e-smith specific Samba configuration files and templates
%define name e-smith-samba
Name: %{name}
%define version 1.13.0
%define release 19sme02
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-samba-1.13.0-03.mitel_patch
Patch1: e-smith-samba-1.13.0-04.mitel_patch
Patch2: e-smith-samba-1.13.0-05.mitel_patch
Patch3: e-smith-samba-1.13.0-06.mitel_patch
Patch4: e-smith-samba-1.13.0-07.mitel_patch
Patch5: e-smith-samba-1.13.0-08.mitel_patch
Patch6: e-smith-samba-1.13.0-09.mitel_patch
Patch7: e-smith-samba-1.13.0-11.mitel_patch
Patch8: e-smith-samba-1.13.0-12.mitel_patch
Patch9: e-smith-samba-1.13.0-13.mitel_patch
Patch10: e-smith-samba-1.13.0-14.mitel_patch
Patch11: e-smith-samba-1.13.0-15.mitel_patch
Patch12: e-smith-samba-1.13.0-16.mitel_patch
Patch13: e-smith-samba-1.13.0-17.mitel_patch
Patch14: e-smith-samba-1.13.0-18.mitel_patch
Patch15: e-smith-samba-1.13.0-19.mitel_patch
Patch16: e-smith-samba-1.13.0-UTF8.patch
Patch17: e-smith-samba-1.13.0-UTF8.patch2
Packager: e-smith developers <bugs@e-smith.com>
Obsoletes: e-smith-netlogon
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools >= 1.13.1-03
Requires: e-smith-lib >= 1.15.1-16
AutoReqProv: no

%changelog
* Sat Jul 16 2005 Shad L. Lords <slords@mail.com>
- [1.13.0-19sme02]
- Change template fragment to default to UTF8 as well

* Sat Jul 16 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.13.0-19sme01]
- Default smb{UnixCharSet} == UTF8
- If smb record exists (i.e. upgrade), but UnixCharSet is not defined,
  set it to ISO8859-1 to maintain filenames on upgrade [SF: 1204695]

* Wed Jun 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-19]
- Restart nmbd during workgroup-update event. [SF: 1220928]

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-18]
- Need to open accounts db r/w in create-machine-account script.

* Thu Mar 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-17]
- Fix missing "use" in create-machine-account script.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-16]
- Last fix was wrong. Real problem was typo in default property setup.
- Remove redundent restart-samba action.

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-15]
- Fix typo in workgroup property lookup in workgroup panel.

* Sun Mar 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-14]
- Group mapping fix from Shad. [MN00070553]

* Fri Mar 11 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-13]
- Add service entries for smbd and nmbd, which slave their own
  status from the smb entry. This allows the generic service
  restart stuff to work. [MN00065576]
- Fix dangling restart-dhcpd symlink. [MN00064130]

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-12]
- Unify the three group mapping scripts into one. [MN00070553]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-11]
- Fix template expansion location of smb.conf [MN00063515]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-10]
- Fix typo in post scriptlet. [MN00063515]

* Tue Feb 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-09]
- Add domain group mapping, contributed by Shad/Greg. [MN00070553]
- Remove anachronisms in create-machine-account script.

* Fri Feb 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-08]
- Fix small template breakages if $LocalIP is not defined.
- Fix warnings from post install script. [MN00070549]
- Remove obsolete "domain admin group" entry from /etc/smb.conf template.
  [MN00063515]
- Revert to standard /etc/samba/smb.conf location for config file.
  [MN00063515]

* Fri Feb 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-07]
- Fix various smb.conf template expansion probs. [MN00063515]

* Fri Feb 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-06]
- Fix typo in template fragment. Commit new files omitted from previous
  checkin in error. [MN00063515]

* Thu Feb 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-05]
- Update samba configuration to use samba 3 features. Update to
  current APIs. [MN00063515]
- Start nmbd before smbd. [MN00070113]

* Thu Feb 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-04]
- Use defaults mechanism to initialise database entries, and migrate
  fragment to convert from deprecated db entries to current style
  Obsolete conf-netlogon script. [MN00062545]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]
- Use generic service adjust action for reload/restart. [MN00065576]

* Mon Feb  7 2005 Charlie Brady <charlieb@e-smith.com>
- [1.13.0-03]
- Run smbd and nmbd's multilogs as smelog user. [MN00063836]

* Thu Feb  5 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-02]
- Updated build dependencies. [msoulier 10992]

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.13.0-01]
- rolling to dev - 1.13.0

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.12.0-01]
- rolling to stable - 1.12.0

* Wed Feb  4 2004 Mark Knox <markk@e-smith.com>
- [1.11.0-16]
- Include rc1.d/K35smb symlink for proper shutdown in single user mode
  [markk 10958]

* Tue Nov 25 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-15]
- Removing client driver option, to move to [printers] section.
  [msoulier 10623]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-14]
- Rolling again to pick up genfilelist change. [msoulier 10648]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-13]
- Moved the e-smith-smb script to supervise/smb, to plan ahead.
  [msoulier 6442]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-12]
- Stopped sourcing /etc/sysconfig/samba, and fixed a syntax error in the
  initscript. [msoulier 6442]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-11]
- Rollback on serviceControl-using scripts. They were not broken.
  [msoulier 6442]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-10]
- Changed the action script code for the new initscript. [msoulier 6442]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Tweaked the smbd run script, and e-smith-smb. [msoulier 6442]

* Mon Nov 17 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-08]
- Added e-smith-smb wrapper to manage both services. [msoulier 6442]

* Sun Nov 16 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-07]
- Added run files for multilog. [msoulier 6442]

* Sun Nov 16 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-06]
- Fixing broken specfile resulting in near-empty filelist. [msoulier 6442]

* Fri Nov 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-05]
- Added supervision of smbd and nmbd. First attempt. [msoulier 6442]
- Updated createlinks script for new build library.

* Fri Nov 14 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-04]
- Added "use client driver" to printer conf. [msoulier 10623]

* Fri Nov  7 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-03]
- *sigh* Really added this time. TGIF. [msoulier 10486]

* Fri Nov  7 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-02]
- Added a "deadtime" option to kill connections, by default, after one week if
  they are no longer active. [msoulier 10486]

* Fri Nov  7 2003 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- rolling to dev stream - 1.11.0

* Thu Sep 11 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.10.0-04]
- Relocated /etc/secrets.tdb to /etc/samba [gordonr 9759]

* Wed Sep 10 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.10.0-03]
- Always return "logon path" line, so that we return
  "logon path =" if roaming profiles are off [gordonr 9913]

* Wed Jul  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.10.0-02]
- Use samba defaults for preferred master and local master [gordonr 9208]
- Turn on wins support if we are the domain master [gordonr 9208]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Wed Jun 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-32]
- Fix confusion in smb{DomainMaster} w.r.t. netlogons [gordonr 9064]

* Thu Jun 12 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-31]
- Added missing 02setupDomainMaster [gordonr 5053]
- Corrected 11winsServer to deal with WINSServer == me [gordonr 5053]

* Fri May 30 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-30]
- Removed dangling symlink to conf-samba-startup. [msoulier 8808]

* Wed May 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-29]
- Move smbpasswd file to /etc/samba/smbpasswd [gordonr 8747]

* Mon May 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-28]
- Added 'type' default fragment for the smb service. [charlieb 8785]

* Wed May 21 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-27]
- fix en-us, fr and es roaming profile text [lijied 5311]

* Tue May 20 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-26]
- Don't worry if the use doesn't have a profile directory [gordonr 6414]

* Tue May 20 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-25]
- Added a defaults fragment. [msoulier 8785]
- Removed conf-samba-startup. [msoulier 8785]

* Thu May 15 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-24]
- Made use of esmith::ConfigDB::wins_server [gordonr 5053]

* Tue May 13 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-23]
- Rationalised smb{WINSServer} and smb{DomainMaster} handling [gordonr 5053]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-22]
- Add Spanish lexicon for workgroup [lijied 3793]

* Mon Apr 14 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-21]
- preferred master should not be set if WINSServer is set [gordonr 6849]

* Mon Apr 14 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-20]
- Limited the workgroup name to 15 characters [lijied 4971]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-19]
- Changed workgroup and servername to lower case again [lijied 7371]

* Wed Apr  9 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-18]
- Fixed french lexicon for workgroup question. [msoulier 5311]

* Wed Apr  9 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-17]
- Changed workgroup and servername to lower case before validation
  and storage [lijied 7371]

* Mon Apr  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-16]
- Create new netlogon directory before trying to relocate netlogon.bat
  [gordonr 8060]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-15]
- Removed Mitel Networks branding [lijied 8016]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-14]
- Fix c&p error in %pre [gordonr 5241]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-13]
- Do the relocation in the SPEC file so we don't have a stray
  directory [gordonr 5241]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-12]
- Relocate netlogon.bat -> /home/e-smith/files/samba/netlogon/netlogon.bat
  [gordonr 5241]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-11]
- Removed conf-dhcpd symlinks - now done in run script [gordonr 7771]

* Fri Mar 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-10]
- Re-worded the text in the workgroup panel. [msoulier 5311]
- Added french translation of that re-wording. [msoulier 5311]

* Fri Mar 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-09]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Tue Mar 11 2003 Mike Dickson <miked@e-smith.com>
- [1.9.0-08]
- restricted length of workgroup entry to 15 characters [miked 4388]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-07]
- Modified workgroup panel order [lijied 7356]

* Wed Mar  5 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-06]
- Split en-us lexicon from workgroup panel [lijied 4030]

* Fri Feb 28 2003 Lijie Deng <lijied@e-smith.com>
- [1.9.0-05]
- Added French lexicon for workgroup. [lijied 5003]

* Wed Jan 29 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-04]
- Delete obsolete special case "primary" fragment in smb.conf.
  [charlieb 5652]

* Thu Jan  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-03]
- Split conf-samba-startup from e-smith-base/conf-startup 
- Relocated reload-samba from e-smith-base [gordonr 5509]

* Mon Dec  9 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-02]
- updates for new UI [miked 5494]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [1.9.0-01]
- Changing to development stream; version upped to 1.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Tue Oct  8 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-08]
- Removed stray DESCRIPTION tag from panel [markk 5135]

* Thu Sep 19 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-07]
- Fix i-bay section of smb.conf template [charlieb 4949]

* Fri Sep 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.2-06]
- Allow smb|WINSServerOverride property which is automagically pushed into
  the smb|WINSServer property before expanding Samba templates [gordonr 4590]

* Fri Sep 13 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.7.2-05]
- Allow domain master setting if smb|WINSServer set to this box [gordonr 4840]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-04]
- Minor refactoring of the last change [markk 3786]

* Tue Sep 10 2002 Mark Knox <markk@e-smith.com>
- [1.7.2-03]
- Remove deprecated split on pipe [markk 3786]

* Fri Aug 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-02]
- Add -M flag to useradd, to prevent creation of /noexistingpath [charlieb 4660]

* Wed Aug  7 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Change default for oplocks from false to true, and add enable of kernel
  oplocks (although it's the default anyway. [charlieb 4520]

* Wed Jul 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Use PAM password change rather than external passwd program and chat
  script. [charlieb 4433]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to maintained stream number to 1.7.0

* Mon Jun  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.2-01]
- Add "pid directory" template fragment to smb.conf, to make samba 2.2.4
  happy (it otherwise wants to use the non-existent /var/run/samba).
  [charlie 3685]

* Mon Jun  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.1-01]
- Revert the posix locking change to the Profile share. We have rebuilt
  samba 2.2.4 under the 2.2.19 kernel as a better fix to the locking problem.
  [charlie 3685]

* Mon Jun  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 30 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.11-01]
- Disable posix locking for the Profile share, as a workaround for
  some locking wierdness with Win2K when saving roaming profiles.
  [charlie 3685]

* Tue May 28 2002 Kirrily Robert <skud@e-smith.com>
- [1.5.10-01]
- Fixed servername validation so dots are not allowed [skud 3695]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.8-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.7-01]
- Update workgroup panel test code to no longer refer to legacy Samba*
  config entries. [charlieb 3160]

* Wed May 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.6-01]
- Migrate obsolete Samba{DomainMaster,Workgroup,ServerName} settings
  in conf-samba then delete any of these if found. [charlieb 3160]

* Tue May  7 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- Further rework of the 11logon{Home,Path} fragments to allow setting
  of smb|LogonPath and smb|LogonHome without having to choose 
  smb|RoamingProfiles [gordonr 3072]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.4-01]
- Localise SAVE button [gordonr 3220]
- Added nav bar entries [gordonr 3155]

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.3-01]
- Woops, create empty /etc/e-smith/tests in %build. [charlieb 3343]

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.2-01]
- Remove /etc/e-smith/tests/.dummy, and instead create empty
  /etc/e-smith/tests in %build. [charlieb 3343]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.1-01]
- restart-nmbd should exit 0 nicely if smb service is disabled [gordonr 3325]

* Mon Apr 29 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.0-01]
- Rolling to development stream
- Always set up logon home and logon path. The Samba defaults are not
  particularly useful, and we want them to be defined to empty if
  not defined in the config db and we are not domain master [gordonr 3072]

* Wed Apr 17 2002 Adrian Chung <adrianc@e-smith.com>
- [1.4.2-01]
- Stop workgroup panel from getting and setting old legacy Samba* values.
- Panel now gets/sets 'smb' properties.

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.4.1-01]
- Language en->en-us

* Wed Apr 10 2002 Adrian Chung <adrianc@e-smith.com>
- [1.4.0-01]
- Remerging text change for domain controller setting into i18n'd panel. 
  [mac #3020]

* Wed Apr 10 2002 Kirrily Robert <skud@e-smith.com>
- [1.3.9-01]
- Added i18n'd workgroup panel [skud #3032]

* Tue Apr  9 2002 Adrian Chung <mac@e-smith.com>
- [1.3.8-01]
- Change quoting of %u to use single quotes in addUserScript template for
  smb.conf. [adrianc #3023]

* Wed Apr  3 2002 Adrian Chung <adrianc@e-smith.com>
- [1.3.7-01]
- Quote %u in add user script directive in smb.conf and remove unnecessary
  first line. [adrianc #3023]

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.6-01]
- D'Oh sama -> samba

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.5-01]
- Create missing profiles and printer driver directories

* Tue Apr 02 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.3.4-01]
- fix restart-nmbd to still start if it can't be stopped [tonyc #2764]

* Tue Mar 26 2002 Adrian Chung <adrianc@e-smith.com>
- [1.3.3-01]
- Modify text in web panel to say "leave set to default, or no if another
  server is already performing this function" with respect to domain master
  setting. [mac - #3020]

* Tue Mar 12 2002 Adrian Chung <adrianc@e-smith.com>
- [1.3.2-01]
- Make WINSServer property override value for DomainMaster, PreferredMaster,
  and LocalMaster.

* Tue Mar 12 2002 Adrian Chung <mac@e-smith.com>
- [1.3.1-01]
- rollRPM: Rolled version number to 1.3.1-01. Includes patches up to 1.3.0-02.

* Fri Feb 15 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Migrate Samba* configuration items to properties of the smb service.

* Thu Feb 14 2002 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- rollRPM: Rolled version number to 1.3.0-01. Includes patches up to 1.2.0-02.

* Thu Jan 03 2002 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-02]
- Reconfigure and restart dhcpd in workgroup update event, in case a
  WINS server has been added. See #2364.
- Purge prep section of lots of stuff which is no longer required
  since the rollRPM.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.2.0-01]
- rollRPM: Rolled version number to 1.2.0-01. Includes patches up to 1.1.0-34.

* Tue Dec  4 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-34]
- Adding workgroup panel, removed from e-smith-base.
- Minor text change, s/a Windows server/another server

* Mon Dec 03 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-33]
- Add conf-samba back into post-install event. Required for initial
  password set.

* Fri Nov 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-32]
- Check for user-deleted type in user-delete-profiledir

* Fri Nov 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-31]
- Extra slosh required in 11logonPath

* Fri Nov 30 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-30]
- Changed group of profiles parent directory to shared to make it searchable
- Replaced %N (NIS server) with %L (Netbios name) in 11logon{Home,Path}
- Reinstated [profiles] share and change logon path to use it
- Added action to user-{create,delete} to add/remove the profile subdirectory
- Added action to post-upgrade to create profiles for existing users
- New smb property RoamingProfiles - defaulting to "no" in conf-samba, 
  which disables logon {home,path} and [profiles] share

* Wed Nov 28 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-29]
- Reduced "printer admin" and "domain admin group" to the "admin" user

* Tue Nov 27 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-28]
- Undo the "Adminstrator" => "admin" mapping
- Remove smb.conf fragment which adds reference to smbusers
- Replace smbusers fragment so that the file now says "# this
  file is not used".

* Mon Nov 26 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-27]
- Remove /etc/smbusers - created empty in init-passwords, but never used
  until now

* Mon Nov 26 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-26]
- Templated /etc/samba/smbusers
- Map "Administrator" for domain logons -> admin
- Note: a local (non-domain) logon still gets treated/ignored as guest
- The property smb|AdminstratorAccount (default Administrator) can be
  used to specify an alternate Administrator account when that account is
  renamed on the Win* clients

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-25]
- Make printer$ share writable in the normal way, restricted by Unix
  permissions (admin:admin)

* Tue Nov 20 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-24]
- Make /etc/smbpasswd 0600,admin,root - allows "admin" to join domains 
- create-machine-account: SUID/SGID root - the script is called as 
  "admin" by Samba, but needs to be "root" to add Unix accounts
- create-machine-account: setRealToEffective really become root or locking
  the Unix account fails with "Only root can do that"
- create-machine-account: Auto-create machine account in accounts database.
  This should be fixed by allowing admin to write to the db fragments

* Mon Nov 19 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-23]
- Added extra slosh to strings in 11logon{Home,Path} and fixed c&p typo

* Mon Nov 19 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-22]
- Check for smb|...|LogonHome and smb|...|LogonPath in those fragments
  Default to ~/._winprofile as before, but allow overrides, for example
  set to empty for local profiles. 4.1.2+e-smith-netlogon and 5.0 both 
  defaulted to roaming profiles
- Explicitly return an empty string from some fragments if 
  $SambaDomainMaster=no, just to be tidy
- Used new e-smith-devtools to set /home/e-smith/files/samba to 
  02755,admin,admin and removed explicit chmod from prep

* Thu Nov 15 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-21]
- Commented out code in create-machine-account which called smbpasswd.
- Samba does this by itself, but we may want to enable it later if this 
  script is ever called outside Samba.

* Wed Nov 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-20]
- Moved profiles to ~user/._winprofile - somewhat better that .profile :-)
- Commented out [Profiles] share, since we are no longer using it

* Wed Nov 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-19]
- Made printer driver directories 0755, per "Samba Unleashed"

* Wed Nov 14 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-18]
- Removed conf-samba from post-install - done in bootstrap-console-save
- Moved all profiles (Win9x and WinNT/2K) under ~user/.profile
- Rewrote machine-account-create as an event
- Note: Unfortunately Samba currently requires the user "root" to 
  create machine accounts (i.e. enter "root" as the user on the client machine)
   A SUID script allows 'admin' to do all of the tasks, but the client gets:
  "Unable to add or change accounts on the domain. The account information
  entered does not grant sufficient privilege to create or change accounts".
- Made printer driver directories world-writable

* Mon Nov 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-17]
- %L (logon server) -> %N (this server) in 11logonPath (as for 11logonHome)

* Mon Nov 12 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-16]
- Swapped 11logon{Home,Path}, added extra backslashes - thanks Greg Zartman
  and others

* Fri Nov 9 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-15]
- Left-justified output
- Removed some redundant use esmith::db lines and implied "return" statements

* Fri Nov 2 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-14]
- Suppressed more comments from output file
- Renamed all [global] fragments to 11*

* Fri Nov 2 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-13]
- Hid all commented-out parameters from output file (remove fragments later)
- Removed more comments from output file
- Unified indentation

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-12]
- Added 11level2Oplocks fragment to disable level2 oplocks
- Removed "share modes" options from [netlogon] share and cleaned up template

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-11]
- Added 61Profilesshare fragment

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-10]
- Removed netlogon comments from output file

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-09]
- Protect logon {home,path} with hard quotes and indent to match others

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-08]
- Added printers and profiles directories
- Need to verify permissions on these directories, Darrell had 777 for all

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-07]
- Merged in changes from dmc-mitel-samba-2.2.2-0 - Thanks Darrell May
- Moved machine-account-create from e-smith-base

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-06]
- Merged (and Obsoleted) e-smith-netlogon

* Thu Nov 1 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-05]
- guest ok = no, map to guest = never

* Mon Oct 22 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-04]
- Add action scripts and workgroup web panel plus associated symlinks

* Thu Oct 4 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-03]
- Removed comments from output file

* Thu Oct 4 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-02]
- Removed template-{begin,end}

* Thu Oct 4 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.1.0-01]
- Split from e-smith-base
- This version only contains the smb.conf template fragments

%description
Configuration files and templates for the Samba daemon.

%prep
%setup
# Create web directories
mkdir -p root/etc/e-smith/web/panels/manager/cgi-bin/
# Create event directories
mkdir -p root/etc/e-smith/events/{console-save,bootstrap-console-save}
mkdir -p root/etc/e-smith/events/{{user,group}-{create,delete,modify}}
mkdir -p root/etc/e-smith/events/{ibay-{create,delete,modify{,-servers}}}
mkdir -p root/etc/e-smith/events/{{printer,network}-{create,delete}}
mkdir -p root/etc/e-smith/events/{post-{upgrade,install}}
mkdir -p root/etc/e-smith/events/{workgroup-update,machine-account-create}
mkdir -p root/home/e-smith/files/samba/profiles
mkdir -p root/home/e-smith/files/samba/printers
for dir in W32ALPHA W32MIPS W32PPC W32X86 WIN40
do
    mkdir -p root/home/e-smith/files/samba/printers/${dir}
done
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
mkdir -p root/etc/e-smith/tests
perl createlinks

# Manage supervise and multilog for smbd.
mkdir -p root/service
ln -s ../var/service/smbd root/service/smbd
mkdir -p root/var/service/smbd/supervise
touch root/var/service/smbd/down
mkdir -p root/var/service/smbd/log/supervise
mkdir -p root/var/log/smbd

# Manage supervise and multilog for nmbd.
mkdir -p root/service
ln -s ../var/service/nmbd root/service/nmbd
mkdir -p root/var/service/nmbd/supervise
touch root/var/service/nmbd/down
mkdir -p root/var/service/nmbd/log/supervise
mkdir -p root/var/log/nmbd

touch root/etc/e-smith/templates/etc/smb.conf/ibays/template-begin

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist \
    --dir '/var/service/smbd' 'attr(1755,root,root)' \
    --file '/var/service/smbd/down' 'attr(0644,root,root)' \
    --file '/var/service/smbd/run' 'attr(0755,root,root)' \
    --dir '/var/service/smbd/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/smbd/log' 'attr(1755,root,root)' \
    --file '/var/service/smbd/log/run' 'attr(0755,root,root)' \
    --dir '/var/log/smbd' 'attr(2750,smelog,smelog)' \
    --dir '/var/service/nmbd' 'attr(1755,root,root)' \
    --file '/var/service/nmbd/down' 'attr(0644,root,root)' \
    --file '/var/service/nmbd/run' 'attr(0755,root,root)' \
    --dir '/var/service/nmbd/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/nmbd/log' 'attr(1755,root,root)' \
    --file '/var/service/nmbd/log/run' 'attr(0755,root,root)' \
    --dir '/var/log/nmbd' 'attr(2750,smelog,smelog)' \
    $RPM_BUILD_ROOT \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
if [ -f /home/netlogon/netlogon.bat ]
then
    mkdir -p /home/e-smith/files/samba/netlogon
    mv /home/netlogon/netlogon.bat \
       /home/e-smith/files/samba/netlogon/netlogon.bat
fi

%preun

%post
# Revert to canonical place for smb.conf
if [ -f /etc/smb.conf ]
then
   rm /etc/smb.conf
   ln -s /etc/samba/smb.conf /etc/smb.conf
fi
if [ -L /etc/samba/smb.conf ]
then
   rm /etc/samba/smb.conf
fi
if [ -f /etc/smbusers ]
then
   rm /etc/smbusers
fi
if [ -f /etc/samba/smbpasswd ]
then
   /bin/chown admin.root /etc/samba/smbpasswd
fi
chown -R smelog.smelog /var/log/{smbd,nmbd}

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
