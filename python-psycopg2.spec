%define module psycopg2

Summary:	PostgreSQL database adapter for Python
Name:		python-%{module}
Version:	2.4.4
Release:	2
Group:		Development/Python
License:	GPLv2 and ZPLv2.1 and BSD
Url:		http://www.psycopg.org/psycopg/
Source0:	http://www.psycopg.org/psycopg/tarballs/PSYCOPG-2-4/%{module}-%{version}.tar.gz
Patch0:		psycopg2-2.4.1-link.patch
BuildRequires:	postgresql-devel
BuildRequires:	python-egenix-mx-base
BuildRequires:	pkgconfig(python)
# for DateTime
Requires:	python-egenix-mx-base

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

psycopg2 is an almost complete rewrite of the psycopg 1.1.x branch.

%prep
%setup -qn %{module}-%{version}
%patch0 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS examples/ ChangeLog  LICENSE  README
%{py_platsitedir}/psycopg2*

