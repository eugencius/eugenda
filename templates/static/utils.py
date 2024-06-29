def set_placeholder(field, placeholder):
    field.widget.attrs["placeholder"] = placeholder


def make_pagination(current_page, page_range, max_pages):
    mid_page = max_pages // 2
    start_page = (current_page - mid_page) - 1
    end_page = current_page + mid_page
    total_pages = len(page_range)

    start_page_offset = abs(start_page) if start_page < 0 else 0

    if start_page < 0:
        start_page = 0
        end_page += start_page_offset

    if end_page >= total_pages:
        start_page = start_page - abs(total_pages - end_page)

    return page_range[start_page:end_page]
