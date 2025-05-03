%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Flatpak Permissions Management KCM
Name:		flatpak-kcm
Version:	6.3.4
Release:	%{?git:0.%{git}.}3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/flatpak-kcm
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/flatpak-kcm/-/archive/%{gitbranch}/flatpak-kcm-%{gitbranchd}.tar.bz2#/flatpak-kcm-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/flatpak-kcm-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Package)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(flatpak)
# Renamed after 6.0 2025-05-03
%rename plasma6-flatpak-kcm

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
%{summary}.

%files -f %{name}.lang
%license LICENSES/*
%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_flatpak.so
%{_datadir}/applications/kcm_flatpak.desktop
