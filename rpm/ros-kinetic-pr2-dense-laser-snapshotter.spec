Name:           ros-kinetic-pr2-dense-laser-snapshotter
Version:        1.0.11
Release:        0%{?dist}
Summary:        ROS pr2_dense_laser_snapshotter package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/pr2_dense_laser_snapshotter
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dense-laser-assembler
Requires:       ros-kinetic-pr2-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dense-laser-assembler
BuildRequires:  ros-kinetic-pr2-msgs

%description
Stores the data from a series of laser scan messages in a dense representation,
allowing users to easily perform image-like operations on intensity or range
data. This package is experimental. Expect APIs to change.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Apr 20 2018 Dave Feil-Seifer <dave@cse.unr.edu> - 1.0.11-0
- Autogenerated by Bloom
