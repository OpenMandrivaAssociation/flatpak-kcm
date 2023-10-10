Summary:		Flatpak Permissions Management KCM
Name:		flatpak-kcm
Version:		5.27.8
Release:		2
License:       GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/flatpak-kcm
Source0:		http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
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
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_flatpak.so
%{_datadir}/kpackage/kcms/kcm_flatpak
%{_datadir}/applications/kcm_flatpak.desktop
