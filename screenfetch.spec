%define	_name		screenFetch

Name:		screenfetch
Version:	3.9.1
Release:	2
Summary:	Screenfetch is a "Bash Screenshot Information Tool"
License:	GPLv3
Group:		Monitoring
Url:		https://github.com/KittyKatt/screenFetch
Source:		https://github.com/KittyKatt/screenFetch/archive/v%{version}/%{_name}-%{version}.tar.gz

BuildArch:	noarch

Recommends:	scrot

%description
screenFetch is a "Bash Screenshot Information Tool". This handy Bash
script can be used to generate one of those nifty terminal theme
information + ASCII distribution logos you see in everyone's screenshots
nowadays. It will auto-detect your distribution and display an ASCII
version of that distribution's logo and some valuable information to the
right. There are options to specify no ascii art, colors, taking a
screenshot upon displaying info, and even customizing the screenshot
command! This script is very easy to add to and can be easily extended.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
install -D -m 755 %{name}-dev %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING README.mkdn CHANGELOG TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
