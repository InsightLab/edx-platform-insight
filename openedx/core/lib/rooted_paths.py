"""Provides rooted_glob, for finding relative glob paths in another director."""

from __future__ import absolute_import
import glob2


def rooted_glob(root, glob):
    """
    Returns the results of running `glob` rooted in the directory `root`.
    All returned paths are relative to `root`.

    Uses glob2 globbing
    """
    return remove_root(root, sorted(glob2.glob('{root}/{glob}'.format(root=root, glob=glob))))


def remove_root(root, paths):
    """
    Returns `paths` made relative to `root`
    """
    return [pth.replace(root + '/', '') for pth in paths]
