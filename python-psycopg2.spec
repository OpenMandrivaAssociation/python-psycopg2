%define module psycopg2

Summary:        PostgreSQL database adapter for Python
Name:           python-%module
Version:        2.4.4
Release:        1
Group:          Development/Python
License:        GPLv2 and ZPLv2.1 and BSD
URL:            http://www.psycopg.org/psycopg/
Source0:        http://www.psycopg.org/psycopg/tarballs/PSYCOPG-2-4/%{module}-%{version}.tar.gz
Patch0:		psycopg2-2.4.1-link.patch
# for DateTime
Requires:       python-egenix-mx-base
BuildRequires:  python-devel
BuildRequires:  postgresql-devel
BuildRequires:  python-egenix-mx-base

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

psycopg2 is an almost complete rewrite of the psycopg 1.1.x branch.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install --root=%buildroot

%files
%doc AUTHORS examples/ ChangeLog  LICENSE  README
%py_platsitedir/psycopg2*


%changelog
* Tue Feb 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.4.4-1
+ Revision: 773927
- version update 2.4.4

* Thu May 12 2011 Funda Wang <fwang@mandriva.org> 2.4.1-1
+ Revision: 673703
- new version 2.4.1

* Tue Dec 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.2-1mdv2011.0
+ Revision: 625615
- update to new version 2.3.2

* Tue Nov 30 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 603245
- fix linkage

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.2.2

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 2.0.13-3mdv2011.0
+ Revision: 592882
- fix file list

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.13-1mdv2010.1
+ Revision: 462522
- update to new version 2.0.13

* Sun Aug 09 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.12-1mdv2010.0
+ Revision: 413417
- update to new version 2.0.12

* Mon May 18 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.11-1mdv2010.0
+ Revision: 377268
- Update to new version 2.0.11

* Thu Mar 05 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.9-1mdv2009.1
+ Revision: 349096
- Update to new version 2.0.9

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 2.0.8-1mdv2009.1
+ Revision: 324057
- New upstream release

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.0.7-2mdv2009.0
+ Revision: 269038
- rebuild early 2009.0 package (before pixel changes)

* Sun May 04 2008 Frederik Himpe <fhimpe@mandriva.org> 2.0.7-1mdv2009.0
+ Revision: 200808
- New upstream version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 2.0.6-1mdv2008.0
+ Revision: 53010
- Import python-psycopg2

