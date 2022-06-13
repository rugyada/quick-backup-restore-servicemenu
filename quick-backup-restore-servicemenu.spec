%define name quick-backup-restore-servicemenu
%define version 1.0
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
License: Creative Commons Attribution
Group: Graphical desktop/KDE
Summary: Create a backup copy for Dolphin context menu
Url: https://store.kde.org/p/1172758
Source:%{name}-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
A couple of service menu to quickly create a backup copy of the
selected files in the same folder, adding a .bak extension,
and to restore them.

%prep
%setup -n %{name}-%version

%install
rm -rf %{buildroot}

mkdir %buildroot
mkdir %buildroot/usr
mkdir %buildroot%_bindir
mkdir %buildroot%_datadir
mkdir %buildroot%_datadir/kservices5/
mkdir %buildroot%_datadir/kservices5/ServiceMenus
install -Dm 755 bak.desktop %buildroot%_datadir/kservices5/ServiceMenus/bak.desktop
install -Dm 755 bak-restore.desktop %buildroot%_datadir/kservices5/ServiceMenus/bak-restore.desktop

%clean
rm -rf %{buildroot}

%files
%_datadir/kservices5/ServiceMenus/*desktop
