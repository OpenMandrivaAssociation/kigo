#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

Name:		kigo
Version:	25.12.1
Release:	%{?git:0.%{git}.}1
Summary:	Go board game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		https://www.kde.org/applications/games/kigo/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kigo/-/archive/%{gitbranch}/kigo-%{gitbranchd}.tar.bz2#/kigo-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/kigo-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  7zip
BuildRequires:	gnugo
Requires:	gnugo

%rename plasma6-kigo

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Kigo is an open-source implementation of the popular Go game.

Go is a strategic board game for two players. It is also known as igo
(Japanese), weiqi or wei ch'i (Chinese) or baduk (Korean).
Go is noted for being rich in strategic complexity despite its simple rules.
The game is played by two players who alternately place black and white stones
(playing pieces, now usually made of glass or plastic) on the vacant
intersections of a grid of 19x19 lines (9x9 or 13x13 for easier games).

%files -f %{name}.lang
%{_bindir}/kigo
%{_datadir}/kigo
%{_datadir}/knsrcfiles/kigo-games.knsrc
%{_datadir}/knsrcfiles/kigo.knsrc
%{_datadir}/applications/org.kde.kigo.desktop
%{_datadir}/metainfo/org.kde.kigo.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/config.kcfg/kigo.kcfg
%{_datadir}/qlogging-categories6/kigo.categories
%{_datadir}/qlogging-categories6/kigo.renamecategories
