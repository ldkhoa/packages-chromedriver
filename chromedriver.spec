Name:           chromedriver
Version:        2.30
Release:        1%{?dist}
Summary:        Chrome driver

Group:          Development/Tools
License:        Apache
URL:            http://chromedriver.storage.googleapis.com/index.html
Source0:        http://chromedriver.storage.googleapis.com/%{version}/%{name}_linux64.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      x86_64



%description
ChromeDriver is a standalone server which implements WebDriver's wire protocol for Chromium.
ChromeDriver is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS).  


%prep
/usr/bin/unzip -q %{SOURCE0} -d %{name}-%{version}

%build
echo 'build'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name}-%{version}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}


%changelog
* Wed Sep 06 2017 Anh Nguyen <anh.nguyen@gooddata.com> - 2.30
- QA-6635 Add Chrome Driver v2.30

* Tue Aug 29 2017 Khoa Le <khoa.le@gooddata.com> - 2.31
- QA-6635 Add Chrome Driver v2.31

* Wed Aug 10 2016 Hung Cao Hiep <hung.cao@gooddata.com> - 2.22
- PAAS-4531 Add chrome driver v2.22
