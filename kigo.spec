%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kigo
Version:	17.08.3
Release:	1
Epoch:		1
Summary:	Go board game for KDE
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kigo/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config) cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n) cmake(KF5KDEGames) cmake(KF5DocTools)
BuildRequires:	cmake(KF5KIO) cmake(KF5NewStuff) cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons) cmake(Qt5Core) cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg) cmake(Qt5Widgets)
Requires:	gnugo

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
%{_sysconfdir}/xdg/kigo-games.knsrc
%{_sysconfdir}/xdg/kigo.knsrc
%{_datadir}/applications/org.kde.kigo.desktop
%{_datadir}/kxmlgui5/kigo
%{_datadir}/metainfo/org.kde.kigo.appdata.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/config.kcfg/kigo.kcfg

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
