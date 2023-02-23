Summary:		Flatpak Permissions Management KCM
Name:		flatpak-kcm
Version:		5.27.1
Release:		1
License:       GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/flatpak-kcm
Source0:		http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(flatpak)

%description
%{summary}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kcm_flatpak

%files -f kcm_flatpak.lang
%license LICENSES/*
%dir %{_datadir}/kpackage/kcms/kcm_flatpak
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_flatpak.so
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_flatpak/contents/ui/permissions.qml
%{_datadir}/applications/kcm_flatpak.desktop
