Name:		kigo
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Go board game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kigo/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(ECM)
BuildRequires:	kdelibs-devel
BuildRequires:	libkdegames-devel
BuildRequires:	libkdegames4-devel
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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
