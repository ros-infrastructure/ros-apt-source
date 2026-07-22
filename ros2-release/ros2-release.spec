%if 0%{?fedora:1}
%global dist_no_ver .fc
%global repo_distname fedora
%else
%global dist_no_ver .el
%global repo_distname rhel
%endif

Name:           ros2-release
Version:        1.2.0
Summary:        Packages for ROS 2 main repository configuration
Release: 1%{dist_no_ver}%{?release_suffix}
BuildArch: noarch
License: ASL 2.0
URL: https://github.com/ros-infrastructure/ros-apt-source
Source0: README.md
%if !0%{?fedora:1}
Requires:  epel-release
%endif

Source10:       RPM-GPG-KEY-ROS2
Source20:       ros2.repo
Source21:       ros2-testing.repo



 
%description
This package contains the ROS 2 repository configuration and GPG key.
 
%prep
%setup -q -c -T
cp -a %{SOURCE0} .

sed 's/$distname/%{repo_distname}/g' %{SOURCE20} > %{basename:%{S:20}}
sed 's/$distname/%{repo_distname}/g' %{SOURCE21} > %{basename:%{S:21}}

%build

%install
install -Dp -m 0644 -t %{buildroot}%{_sysconfdir}/pki/rpm-gpg %{S:10}
install -Dp -m 0644 -t %{buildroot}%{_sysconfdir}/yum.repos.d %{basename:%{S:20}} %{basename:%{S:21}}

%files
%doc README.md
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ROS2
%config(noreplace) %{_sysconfdir}/yum.repos.d/ros2.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/ros2-testing.repo
 
%changelog
* Mon Apr 20 2026 Clara Berendsen <claraberendsen@ekumenlabs.com> - 1.2.0-1
- Version bump to add Trixie and Resolute on ros-apt-source. Bump here to keep synchrony.
* Wed May 21 2025 Clara Berendsen - 1.1.0-1
- Version bump to add Debian as supported OS on ros-apt-source. Bump here to keep synchrony. 
* Wed Apr 30 2025 Clara Berendsen - 1.0.0-1
- Initial package creation.
