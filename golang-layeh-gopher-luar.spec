# Run tests in check section
%bcond_without check

%global goipath         layeh.com/gopher-luar
%global forgeurl        https://github.com/layeh/gopher-luar
Version:                1.0.3

%global common_description %{expand:
Custom type reflection for gopher-lua.}

%gometa

Name:    %{goname}
Release: 2%{?dist}
Summary: Custom type reflection for gopher-lua
License: MPLv2.0
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/yuin/gopher-lua)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-1
- Bump to 1.0.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.1-1
- First package for Fedora

