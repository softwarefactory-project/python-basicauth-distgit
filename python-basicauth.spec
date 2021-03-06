%global         sum An incredibly simple HTTP basic auth implementation
%global         uname basicauth

Name:           python-basicauth
Version:        0.3
Release:        2%{?dist}
Summary:        %{sum}

License:        Public Domain
URL:            https://github.com/rdegges/python-basicauth
Source0:        https://pypi.python.org/packages/08/e9/0d1343e98853d984928c7398f9be60b8b068d70e7c82ffed6a7711aa8758/%{uname}-%{version}.tar.gz

BuildArch:      noarch

Buildrequires:  python-nose
Buildrequires:  python-setuptools
Buildrequires:  python2-devel

%description
An incredibly simple HTTP basic auth implementation

%package -n python2-basicauth
Summary:        %{sum}

Buildrequires:  python-nose
Buildrequires:  python-setuptools
Buildrequires:  python2-devel

%description -n python2-basicauth
An incredibly simple HTTP basic auth implementation

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v tests.py

%files -n python2-basicauth
%{python2_sitelib}/*

%changelog
* Tue Feb 22 2017 Fabien Boucher <fboucher@redhat.com> - 0.3-2
- Fix package name

* Tue Feb 21 2017 Nicolas Hicher <nhicher@redhat.com> - 0.3-1
- Initial packaging
