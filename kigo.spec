Name:		kigo
Version:	4.10.2
Release:	1
Epoch:		1
Summary:	Go board game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kigo/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
Requires:	gnugo

%description
Kigo is an open-source implementation of the popular Go game.

Go is a strategic board game for two players. It is also known as igo
(Japanese), weiqi or wei ch'i (Chinese) or baduk (Korean).
Go is noted for being rich in strategic complexity despite its simple rules.
The game is played by two players who alternately place black and white stones
(playing pieces, now usually made of glass or plastic) on the vacant
intersections of a grid of 19x19 lines (9x9 or 13x13 for easier games).

%files
%{_kde_bindir}/kigo
%{_kde_applicationsdir}/kigo.desktop
%{_kde_appsdir}/kigo
%{_kde_datadir}/config.kcfg/kigo.kcfg
%{_kde_configdir}/kigo-games.knsrc
%{_kde_configdir}/kigo.knsrc
%{_kde_docdir}/HTML/en/kigo
%{_kde_iconsdir}/*/*/apps/kigo.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

