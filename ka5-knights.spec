%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		knights
Summary:	knights
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ef443fabc0246738de534c4ef44ce0a6
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-kplotting-devel >= 5.30.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.30.0
BuildRequires:	kf5-kwallet-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	kf5-plasma-framework-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNights is a chess game. As a player, your goal is to defeat your
opponent by checkmating their king.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/knights.categories
/etc/xdg/knights.knsrc
%attr(755,root,root) %{_bindir}/knights
%{_desktopdir}/org.kde.knights.desktop
%{_datadir}/config.kcfg/knights.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_iconsdir}/hicolor/16x16/apps/knights.png
%{_iconsdir}/hicolor/32x32/apps/knights.png
%{_iconsdir}/hicolor/48x48/apps/knights.png
%{_iconsdir}/hicolor/64x64/apps/knights.png
%{_datadir}/knights
%{_datadir}/kxmlgui5/knights
%{_datadir}/metainfo/org.kde.knights.appdata.xml
