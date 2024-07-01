from django.core.paginator import Paginator


def set_placeholder(field, placeholder):
    field.widget.attrs["placeholder"] = placeholder


def make_pagination_range(current_page, page_range, max_pages):
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


def make_pagination(request, queryset, per_page, max_pages=6):
    current_page = int(request.GET.get("page", 1))

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    if len(paginator.page_range) < max_pages:
        page_range = paginator.page_range
    else:
        page_range = make_pagination_range(
            current_page, paginator.page_range, max_pages=max_pages
        )

    return page_obj, page_range, current_page
