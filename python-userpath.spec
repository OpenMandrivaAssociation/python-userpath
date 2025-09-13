Name:		python-userpath
Version:	1.9.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/u/userpath/userpath-%{version}.tar.gz
Summary:	Cross-platform tool for adding locations to the user PATH
URL:		https://pypi.org/project/userpath/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Cross-platform tool for adding locations to the user PATH

%files
%{_bindir}/userpath
%{py_sitedir}/userpath
%{py_sitedir}/userpath-*.*-info
