%define name    screenfetch 
%define oname    screenFetch
%define version 3.8.0

Name:           %{name}
Version:        %{version}
Release:        1
Summary: 	Screen-shot information tool for nerds
License: 	GPLv3
Group: 		Shells
Url:		http://github.com/KittyKatt/screenFetch
Source0:	%{oname}-%{version}.tar.gz
BuildArch: 	noarch
Provides:	sfetch = %{EVRD}
Provides:	screenfetch = %{EVRD}

%description
Script to fetch system and theme settings for screen-shots in most mainstream.

%files
%doc CHANGELOG COPYING README.mkdn TODO
%{_bindir}/*
%{_mandir}/man1/screenfetch.1*
#-----------------------------------------------------------------------
%prep
%setup -qn  %{oname}-%{version}
# clean the shell before launch it.Sflo
sed -i '28iclear' screenfetch

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
# alias , "sfetch" is more handy to use for newbies
# and not only.Sflo
install -m 755 screenfetch %{buildroot}%{_bindir}/
pushd %{buildroot}%{_bindir}
ln -s screenfetch sfetch
popd
install -m 644 -p -D screenfetch.1 %{buildroot}%{_mandir}/man1/screenfetch.1
