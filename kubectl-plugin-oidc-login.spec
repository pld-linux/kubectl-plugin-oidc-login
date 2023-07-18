%define		vendor_version	1.28.0

Summary:	kubectl plugin for Kubernetes OpenID Connect authentication
Name:		kubectl-plugin-oidc-login
Version:	1.28.0
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/int128/kubelogin/archive/v%{version}/kubelogin-%{version}.tar.gz
# Source0-md5:	8d6256e68b9636f5775edadbf4f76de8
Source1:	kubelogin-vendor-%{vendor_version}.tar.xz
# Source1-md5:	f29ed6ed28f543fd05594c9d5d30bf47
URL:		https://github.com/int128/kubelogin
BuildRequires:	golang >= 1.19
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kubectl
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
kubectl plugin for Kubernetes OpenID Connect authentication.

%prep
%setup -q -n kubelogin-%{version} -a1

%{__mv} kubelogin-%{vendor_version}/vendor .

%build
%__go build -v -mod=vendor -o target/kubectl-oidc_login

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p target/kubectl-oidc_login $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/*.{md,svg}
%attr(755,root,root) %{_bindir}/kubectl-oidc_login
