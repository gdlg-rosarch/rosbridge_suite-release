Name:           ros-indigo-rosapi
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS rosapi package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/RobotWebTools/rosbridge_suite
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosbridge-library
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rosbridge-library
BuildRequires:  ros-indigo-rospy

%description
Provides service calls for getting ros meta-information, like list of topics,
services, params, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Oct 08 2014 Brandon Alexander <baalexander@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

* Tue Oct 07 2014 Brandon Alexander <baalexander@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

* Mon Oct 06 2014 Brandon Alexander <baalexander@gmail.com> - 0.6.2-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Brandon Alexander <baalexander@gmail.com> - 0.6.1-0
- Autogenerated by Bloom

