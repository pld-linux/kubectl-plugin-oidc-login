%define		vendor_version	1.31.0

Summary:	kubectl plugin for Kubernetes OpenID Connect authentication
Name:		kubectl-plugin-oidc-login
Version:	1.31.0
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/int128/kubelogin/archive/v%{version}/kubelogin-%{version}.tar.gz
# Source0-md5:	39b4027ab8bad2db62d4efa81bc5ed23
Source1:	kubelogin-vendor-%{vendor_version}.tar.xz
# Source1-md5:	9b94bfa9bc37aa2b2560179fea2f4924
URL:		https://github.com/int128/kubelogin
BuildRequires:	golang >= 1.23.2
BuildRequires:	rpmbuild(macros) >= 2.009
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kubectl
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

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
