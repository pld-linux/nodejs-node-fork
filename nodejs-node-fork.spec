%define		pkg	fork
Summary:	Look-alike nodejs 0.6.x child_process.fork() function module
Name:		nodejs-%{pkg}
Version:	0.4.2
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/stolsma/node-fork
Source0:	http://registry.npmjs.org/node-fork/-/node-fork-%{version}.tgz
# Source0-md5:	ac4f32aad046e6ba22d2d36c254570f4
BuildRequires:	nodejs-devel
BuildRequires:	rpmbuild(macros) >= 1.634
# due library being versioned
%requires_eq	nodejs
Requires:	nodejs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Look-alike nodejs 0.6.x child_process.fork() function module for
nodejs 0.4.x and 0.6.x.

%prep
%setup -qc
mv package/* .

%build
node-waf configure build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/lib
cp -p package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p lib/*.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/lib

version=$(node -v)
install -p build/Release/createpair.node $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/lib/createpair.$version.node

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/lib/*.js
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/lib/createpair.v*.node

%{_examplesdir}/%{name}-%{version}
