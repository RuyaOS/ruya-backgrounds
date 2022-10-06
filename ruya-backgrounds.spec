Name: ruya-backgrounds
Version: 1.0
Release: 5%{?dist}
Summary: Ruya backgrounds
Summary(ar): خلفيات رؤية
License: GPLv2
URL: https://parmg.sa
Source0: gpl-2.0.txt
Source1: ruya-bg-001-v3.jpg

Source100: ruya.xml

BuildArch: noarch

%description
Ruya backgrounds

%description -l ar
خلفيات رؤية

%prep
cp %{SOURCE0} .

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/RUYA
mkdir -p %{buildroot}%{_datadir}/gnome-background-properties
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/backgrounds/RUYA
install -Dp -m 0644 %{SOURCE100} %{buildroot}%{_datadir}/gnome-background-properties
%files
%license gpl-2.0.txt
%{_datadir}/backgrounds/RUYA/*
%{_datadir}/gnome-background-properties/ruya.xml

%changelog
* Thu Mar 24 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1.0-5
- Initial
