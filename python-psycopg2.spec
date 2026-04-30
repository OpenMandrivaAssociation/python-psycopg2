%define module psycopg2

Name:		python-psycopg2
Summary:	PostgreSQL database adapter for Python
Version:	2.9.12
Release:	2
Group:		Development/Python
License:	LGPL-3.0-or-later
URL:		https://www.psycopg.org/psycopg/
Source0:  https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	postgresql-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

psycopg2 is an almost complete rewrite of the psycopg 1.1.x branch.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver} -lm"

%files
%doc AUTHORS NEWS README.rst
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}*.*-info
