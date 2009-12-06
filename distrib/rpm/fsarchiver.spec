Name:		fsarchiver
Version:	0.6.0
Release:	1%{?dist}
Summary:	Safe and flexible file-system backup/deployment tool

Group:		Applications/Archiving
License:	GPLv2
URL:		http://www.fsarchiver.org
Source0:  	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz      
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	e2fsprogs-devel => 1.41.4
BuildRequires:	e2fsprogs
BuildRequires:	libattr-devel
BuildRequires:  libgcrypt-devel	
BuildRequires:	zlib-devel
BuildRequires:	bzip2-devel
BuildRequires:	lzo-devel
# Disabled because it needs a beta release of lzma which we do not ship
#BuildRequires:	lzma-devel

%description
FSArchiver is a system tool that allows you to save the contents of a 
file-system to a compressed archive file. The file-system can be restored 
on a partition which has a different size and it can be restored on a 
different file-system. Unlike tar/dar, FSArchiver also creates the 
file-system when it extracts the data to partitions. Everything is 
checksummed in the archive in order to protect the data. If the archive 
is corrupt, you just loose the current file, not the whole archive.

%prep
%setup -q

%build
%configure --disable-lzma
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%doc COPYING README THANKS NEWS

%changelog
* Sun Sep 27 2009 Francois Dupoux <fdupoux@free.fr> - 0.6.0-1
- Update to 0.6.0 and replace openssl with libgcrypt

* Sat Jul 11 2009 Francois Dupoux <fdupoux@free.fr> - 0.5.8-1
- Update to 0.5.8

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.5-2
- BR e2fsprogs

* Tue May 19 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.5-1
- Update to 0.5.5

* Fri May 01 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.5.2-1
- Update to 0.5.2

* Sat Mar 28 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.6-1
- Update to 0.4.6

* Sun Mar 22 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.5-1
- Update to 0.4.5

* Sun Mar 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.4-2
- Fix file section
- Fix changelog

* Sun Mar 07 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 28 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.3-1
- 0.4.3
- Drop build patch, no longer needed

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.1-2
- Fix description

* Thu Feb 12 2009 Adel Gadllah <adel.gadllah@gmail.com> - 0.4.1-1
- Initial package
